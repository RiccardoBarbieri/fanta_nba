export interface Feature {
  name: string,
  available: boolean,
}

export interface Sport {
  name: string,
  features: Feature[],
  url: string | undefined,
}
