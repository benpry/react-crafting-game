import { useEffect, useMemo, useState } from "react";
import { SideBar } from "./components/sidebar";
import { PlaygroundArea } from "./components/playground";
import { ElementCard } from "./components/element-card";
import { Element, PlacedElement } from "./interfaces/element";
import { DndContext, DragOverlay } from "@dnd-kit/core";
import { v4 as uuid } from "uuid";
import axios from "axios";

export default function Home() {
  const [elements, setElements] = useState<Element[]>([]);
  const [placedElements, setPlacedElements] = useState<PlacedElement[]>([]);

  const [activeElement, setActiveElement] = useState<Element | null>(null);
  const [activePlacedElement, setActivePlacedElement] =
    useState<PlacedElement | null>(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/start").then(({ data }) => {
      setElements(data.elements);
    });
  }, []);

  useEffect(() => {
    if (elements.length === 0) return;
    localStorage.setItem("elements", JSON.stringify(elements));
  }, [elements]);

  const handleDragStart = (event: any) => {
    console.log("start event", event);
    const { active } = event;

    if (active.data.current.type === "element") {
      setActiveElement(event.active.data.current.element);
    } else if (active.data.current.type === "placed-element") {
      setActivePlacedElement(event.active.data.current.element);
    }
  };

  const handleCombineElements = (
    e1: PlacedElement,
    e2: PlacedElement | Element,
  ) => {
    if ("id" in e2) {
      // Remove e2 and set e1 to loading
      setPlacedElements((prev) =>
        prev
          .filter((v) => v.id !== e2.id)
          .map((v) =>
            v.id === e1.id
              ? {
                  ...v,
                  isLoading: true,
                }
              : v,
          ),
      );
    } else {
      setPlacedElements((prev) =>
        prev.map((v) =>
          v.id === e1.id
            ? {
                ...v,
                isLoading: true,
              }
            : v,
        ),
      );
    }

    axios
      .post("http://127.0.0.1:8000/api/combine", {
        item1: e1.text,
        item2: e2.text,
      })
      .then(({ data }) => {
        setPlacedElements((prev) =>
          // Replace e1 with the new element
          prev.map((v) =>
            v.id === e1.id
              ? {
                  ...data.element,
                  id: uuid(),
                  x: v.x,
                  y: v.y,
                  isLoading: false,
                }
              : v,
          ),
        );
        // If the created element is new, add it to the elements list
        if (elements.every((element) => element.text !== data.element.text)) {
          setElements((prev) => [...prev, data.element]);
        }
      })
      .catch((e) => {
        window.alert(
          "Something when wrong! Failed to combine elements" + e.toString(),
        );
        setPlacedElements((prev) =>
          prev.map((v) =>
            v.id === e1.id
              ? {
                  ...v,
                  isLoading: false,
                }
              : v,
          ),
        );
      });
  };

  const handleDragEnd = (event: any) => {
    const { active, over } = event;

    console.log("active", active);
    console.log("over", over);

    if (
      active.data.current.type === "placed-element" &&
      over &&
      over.data.current.type === "sidebar"
    ) {
      // remove the element from the game
      const element = active.data.current.element;
      const newPlacedElements = placedElements.filter(
        (v) => v.id !== element.id,
      );
      setPlacedElements(newPlacedElements);
    } else if (
      active.data.current.type === "placed-element" &&
      over &&
      over.data.current.type === "placed-element"
    ) {
      // combine the elements
      handleCombineElements(
        over.data.current.element,
        active.data.current.element,
      );
    } else if (active.data.current.type === "placed-element") {
      // place the already-placed element on the playground
      const element = active.data.current.element;
      const newPlacedElements = placedElements.map((v) =>
        v.id === element.id
          ? {
              ...element,
              x: element.x + event.delta.x,
              y: element.y + event.delta.y,
            }
          : v,
      );
      setPlacedElements(newPlacedElements);
    }

    if (
      active.data.current.type === "element" &&
      over &&
      over.data.current.type === "playground"
    ) {
      const element = active.data.current.element;
      // get the bounding box

      const target = event.activatorEvent.target;
      let elementRect;
      if (target.classList.contains("flex")) {
        elementRect = event.activatorEvent.target.getBoundingClientRect();
      } else {
        elementRect = target.parentElement.getBoundingClientRect();
      }

      const placedElement = {
        ...element,
        id: uuid(),
        x: elementRect.left,
        y: elementRect.top,
      };
      setPlacedElements((prev) => [...prev, placedElement]);
    } else if (
      active.data.current.type === "element" &&
      over &&
      over.data.current.type === "placed-element"
    ) {
      handleCombineElements(
        over.data.current.element,
        active.data.current.element,
      );
    }

    setActiveElement(null);
    setActivePlacedElement(null);
  };

  const isLoading = useMemo(() => {
    return placedElements.some((v) => v.isLoading);
  }, [placedElements]);

  return (
    <DndContext onDragStart={handleDragStart} onDragEnd={handleDragEnd}>
      <main className="flex h-screen flex-col border-4 border-black">
        <div className="grid grid-cols-12 h-full">
          <PlaygroundArea
            setElements={setElements}
            setPlacedElements={setPlacedElements}
            placedElements={placedElements}
            isLoading={isLoading}
          />
          <SideBar elements={elements} isLoading={isLoading} />
        </div>
      </main>
      <DragOverlay dropAnimation={null}>
        {activeElement && <ElementCard element={activeElement} />}
        {activePlacedElement && <ElementCard element={activePlacedElement} />}
      </DragOverlay>
    </DndContext>
  );
}
