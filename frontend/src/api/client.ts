export interface ApiClient {
  get<T>(path: string): Promise<T>
}

export const apiClient: ApiClient = {
  async get<T>(path: string): Promise<T> {
    throw new Error(`Not implemented: GET ${path}`)
  },
}
