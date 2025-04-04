import { useDraggable, useDroppable } from "@dnd-kit/core";
import { Element, PlacedElement } from "../interfaces/element";
import { Loader } from "lucide-react";
import { CSS } from "@dnd-kit/utilities";
import { useMemo } from "react";
import { isPlacedElement } from "../interfaces/element";

export const ElementCard = ({
  element,
}: {
  element: Element | PlacedElement;
}) => {
  const bgColor = element.durable ? "bg-slate-200" : "bg-white";
  const toColor = element.durable ? "to-slate-200" : "to-white";
  const fixedClasses = `flex gap-2 p-2 border ${bgColor} border-slate-400 rounded-md text-xl h-fit w-fit hover:bg-gradient-to-t from-cyan-100 ${toColor}`;

  const classes = `${fixedClasses} hover:bg-cyan-100`;
  const id = isPlacedElement(element) ? element.id : undefined;

  return (
    <div className={classes} id={id}>
      <div className="pointer-events-none">{element.emoji} {element.name}</div>
      <div className="pointer-events-none">{element.value}</div>
    </div>
  );
};

export const ElementCardSideBarWrapper = ({
  element,
  isLoading,
}: {
  element: Element;
  isLoading: boolean;
}) => {
  const { attributes, listeners, setNodeRef, transform } = useDraggable({
    id: element.name,
    data: {
      element,
      type: "element",
    },
    disabled: isLoading,
  });

  const style = {
    transform: CSS.Translate.toString(transform),
  };

  return (
    <div
      ref={setNodeRef}
      style={style}
      className="w-fit h-fit"
      onMouseDown={(e) => {
        e.preventDefault();
      }}
      {...listeners}
      {...attributes}
    >
      <ElementCard element={element} />
    </div>
  );
};

export const ElementCardDraggableWrapper = ({
  element,
  isLoading,
}: {
  element: PlacedElement;
  isLoading: boolean;
}) => {
  const { attributes, listeners, setNodeRef, transform } = useDraggable({
    id: element.id,
    data: {
      element,
      type: "placed-element",
    },
    disabled: isLoading,
  });

  const { setNodeRef: setNodeRef2 } = useDroppable({
    id: element.id,
    data: {
      element,
      type: "placed-element",
    },
    disabled: isLoading,
  });

  const style = useMemo(
    () => ({
      transform: CSS.Translate.toString(transform),
      top: element.y,
      left: element.x,
    }),
    [element.x, element.y, transform],
  );

  const classes = "absolute w-fit h-fit";

  return (
    <div
      ref={setNodeRef}
      className={classes}
      style={style}
      {...listeners}
      {...attributes}
    >
      <div ref={setNodeRef2}>
        {element.isLoading && (
          <div className="flex gap-2 p-2 border bg-white border-slate-400 rounded-md text-xl h-fit w-fit">
            <div>
              <Loader className="animate-spin inline-block" />
            </div>
            <div>combining...</div>
          </div>
        )}
        {!element.isLoading && <ElementCard element={element} />}
      </div>
    </div>
  );
};
