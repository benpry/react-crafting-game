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
    <div className="col-span-3 border-l relative" ref={setNodeRef}>
      <div className="absolute inset-0 flex flex-col">
        <h2 className="text-lg text-center font-semibold">Inventory</h2>
        <div className="overflow-y-auto flex-1">
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
    </div>
  );
};
