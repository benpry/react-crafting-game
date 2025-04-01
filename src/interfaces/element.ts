export interface Element {
    name: string;
    emoji: string;
    value: number;
    consumable: boolean;
}

export interface PlacedElement extends Element {
    id: string;
    x: number;
    y: number;
    isLoading?: boolean;
}

export function isPlacedElement(object: any): object is PlacedElement {
    return "id" in object && "x" in object && "y" in object;
}
