export interface Element {
    text: string;
    image: string;
    discovered: boolean;
}

export interface PlacedElement extends Element {
    id: string;
    x: number;
    y: number;
    isLoading?: boolean;
}
