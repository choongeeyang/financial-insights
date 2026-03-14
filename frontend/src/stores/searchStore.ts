import { create } from "zustand";

// Defines the structure of the search store
interface SearchState {
  query: string;                 // current search query
  setQuery: (q: string) => void; // function to update query
  clear: () => void;             // function to reset query
}

// Create a Zustand store for managing search state
export const useSearchStore = create<SearchState>((set) => ({
  query: "",                     // initial query value

  // Update the search query
  setQuery: (q) => set({ query: q }),

  // Clear the search query
  clear: () => set({ query: "" }),
}));