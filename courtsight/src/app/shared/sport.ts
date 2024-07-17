export interface Feature {
  name: string,
  available: boolean,
}

export interface AvailableSport {
  name: string,
  features: Feature[],
  url: string | undefined,
}

export interface Sport {
  key: string,
  active: boolean,
  group: string,
  description: string,
  title: string,
  has_outrights: boolean,
}
