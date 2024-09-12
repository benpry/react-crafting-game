"use client";
import { Element, PlacedElement } from "../interfaces/element";
import { ElementCardDraggableWrapper } from "./element-card";
import { useDroppable } from "@dnd-kit/core";

export const PlaygroundArea = ({
  placedElements,
  isLoading,
}: {
  placedElements: PlacedElement[];
  setPlacedElements: (v: PlacedElement[]) => void;
  setElements: (v: Element[]) => void;
  isLoading: boolean;
}) => {
  const { setNodeRef } = useDroppable({
    id: "playground-area",
    data: {
      type: "playground",
    },
    disabled: isLoading,
  });

  return (
    <div className="col-span-9 h-full w-full relative" ref={setNodeRef}>
      {placedElements.map((element, index) => (
        <ElementCardDraggableWrapper
          key={index}
          element={element}
          isLoading={isLoading}
        />
      ))}
    </div>
  );
};
