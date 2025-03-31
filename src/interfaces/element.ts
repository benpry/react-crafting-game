export interface Element {
    text: string;
    image: string;
    value: number;
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
