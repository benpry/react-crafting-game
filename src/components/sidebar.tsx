import { Element } from "../interfaces/element";
import { ElementCardSideBarWrapper } from "./element-card";
import { useDroppable } from "@dnd-kit/core";

export const SideBar = ({
  elements,
  isLoading,
}: {
  elements: Element[];
  isLoading: boolean;
}) => {
  const { setNodeRef } = useDroppable({
    id: "sidebar-area",
    data: {
      type: "sidebar",
    },
    disabled: isLoading,
  });

  return (
    <div
      className="col-span-3 border-l h-screen flex flex-col"
      ref={setNodeRef}
    >
      <div className="flex flex-1 justify-start items-start overflow-y-scroll overflow-x-hidden">
        <div className="flex flex-wrap gap-2 p-2">
          {elements.map((element) => (
            <ElementCardSideBarWrapper
              key={element.text}
              element={element}
              isLoading={isLoading}
            />
          ))}
        </div>
      </div>
    </div>
  );
};
