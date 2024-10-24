"use client";
import { PlacedElement } from "../interfaces/element";
import { ElementCardDraggableWrapper } from "./element-card";
import { useDroppable } from "@dnd-kit/core";
import { Trash } from "lucide-react";

export const PlaygroundArea = ({
  placedElements,
  setPlacedElements,
  isLoading,
}: {
  placedElements: PlacedElement[];
  setPlacedElements: (v: PlacedElement[]) => void;
  isLoading: boolean;
}) => {
  const { setNodeRef } = useDroppable({
    id: "playground-area",
    data: {
      type: "playground",
    },
    disabled: isLoading,
  });

  const onClearPlacedElements = () => {
    setPlacedElements([]);
  };

  return (
    <div className="col-span-9 h-full w-full relative" ref={setNodeRef}>
      {placedElements.map((element, index) => (
        <ElementCardDraggableWrapper
          key={index}
          element={element}
          isLoading={isLoading}
        />
      ))}
      <div
        className="absolute bottom-0 right-0 p-4 cursor-pointer hover:text-red-400"
        onClick={onClearPlacedElements}
      >
        <Trash />
      </div>
    </div>
  );
};
