export const VisibilityFilters = {
  ALL: "all",
  READS: "reads",
  PENDING: "pending"
};

export function getFilteredComicBookListAndCounts(
  comicBookList,
  visibilityFilter
) {
  const readsList = comicBookList.filter(item => item.read);
  const pendingList = comicBookList.filter(item => !item.read);
  let filteredList = comicBookList;

  if (visibilityFilter === VisibilityFilters.READS) {
    filteredList = readsList;
  } else if (visibilityFilter === VisibilityFilters.PENDING) {
    filteredList = pendingList;
  }
  return {
    allCount: comicBookList.length,
    readsCount: readsList.length,
    pendingCount: pendingList.length,
    filteredList
  };
}
