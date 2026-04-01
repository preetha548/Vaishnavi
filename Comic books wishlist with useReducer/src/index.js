import React, { useReducer, useState } from "react";
import ReactDOM from "react-dom";
import { Button, Flex, Heading, TextInput } from "@primer/components";
import {
  List,
  ListItem,
  ComicBookTitle,
  Filters,
  Container
} from "./components";
import { VisibilityFilters, getFilteredComicBookListAndCounts } from "./utils";

const initialComicbookState = {
  comicBookList: [
    { title: "The Amazing Spider-Man #700", read: false },
    { title: "The Immortal Hulk #4", read: false },
    { title: "Sharkey the bounty hunter #1", read: false }
  ],
  visibilityFilter: VisibilityFilters.ALL
};

const ActionTypes = {
  ADD_COMIC_BOOK: "ADD_COMMIC_BOOK",
  TOGGLE_READ_COMIC_BOOK: "TOGGLE_READ_COMIC_BOOK",
  SET_VISIBILITY_FILTER: "SET_VISIBILITY_FILTER"
};

function comicBookReducer(state, action) {
  switch (action.type) {
    case ActionTypes.ADD_COMIC_BOOK:
      return {
        ...state,
        comicBookList: [
          { title: action.comicBook, read: false },
          ...state.comicBookList
        ]
      };
    case ActionTypes.TOGGLE_READ_COMIC_BOOK: {
      const newComicBookList = [...state.comicBookList];
      const comicbook = newComicBookList[action.index];
      comicbook.read = !comicbook.read;
      return {
        ...state,
        comicbookList: newComicBookList
      };
    }
    case ActionTypes.SET_VISIBILITY_FILTER:
      return {
        ...state,
        visibilityFilter: action.visibilityFilter
      };
    default:
      return state;
  }
}

function App() {
  const [comicBook, setComicBook] = useState("");
  const [{ comicBookList, visibilityFilter }, dispatch] = useReducer(
    comicBookReducer,
    initialComicbookState
  );

  const onSubmit = evt => {
    evt.preventDefault();
    if (comicBook === "") return;
    dispatch({ type: ActionTypes.ADD_COMIC_BOOK, comicBook });
    setComicBook("");
  };

  const onComicBookRead = index => {
    dispatch({ type: ActionTypes.TOGGLE_READ_COMIC_BOOK, index });
  };

  const { filteredList, ...counts } = getFilteredComicBookListAndCounts(
    comicBookList,
    visibilityFilter
  );
  return (
    <Container>
      <Heading>Comic Books's Readlist</Heading>
      <form onSubmit={onSubmit} style={{ width: "100%", marginTop: "1rem" }}>
        <Flex>
          <TextInput
            aria-label="comic book"
            name="comic-book"
            placeholder="Your comic book"
            value={comicBook}
            onChange={ev => setComicBook(ev.target.value)}
            marginRight="0.5rem"
            style={{ flexGrow: 1 }}
          />
          <Button type="submit">Add</Button>
        </Flex>
      </form>
      <Filters
        visibilityFilter={visibilityFilter}
        onVisibilityFilterChange={newVisibilityFilter =>
          dispatch({
            type: ActionTypes.SET_VISIBILITY_FILTER,
            visibilityFilter: newVisibilityFilter
          })
        }
        {...counts}
      />

      <List>
        {filteredList.map((item, index) => (
          <ListItem key={`${item.title}_${index}`}>
            <ComicBookTitle read={item.read}>{item.title}</ComicBookTitle>
            <input
              type="checkbox"
              checked={item.read}
              onChange={() => onComicBookRead(index)}
            />
          </ListItem>
        ))}
      </List>
    </Container>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
