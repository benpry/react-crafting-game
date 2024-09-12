import { useDraggable, useDroppable } from "@dnd-kit/core";
import { Element, PlacedElement } from "../interfaces/element";
import { Loader } from "lucide-react";
import { CSS } from "@dnd-kit/utilities";
import { useMemo } from "react";

export const ElementCard = ({ element }: { element: Element }) => {
  return (
    <div className="flex gap-2 p-2 border border-slate-400 rounded-md text-xl h-fit w-fit hover:bg-gradient-to-t from-cyan-100 to-white">
      <img className="w-8 h-8" src={`public/assets/${element.image}.svg`}></img>
      <div>{element.text}</div>
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
    id: element.text,
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

  const { isOver, setNodeRef: setNodeRef2 } = useDroppable({
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

  const classes = isOver
    ? "absolute w-fit h-fit bg-gradient-to-t from-cyan-100 to-white"
    : "absolute w-fit h-fit";

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
          <div className="flex gap-2 px-2 border rounded-xl h-fit w-fit">
            <div>
              <Loader className="animate-spin inline-block" />
            </div>
            <div>combining</div>
          </div>
        )}
        {!element.isLoading && <ElementCard element={element} />}
      </div>
    </div>
  );
};
