import React from "react";
import { BaseStyles, Flex, FilterList } from "@primer/components";
import styled from "styled-components";
import { VisibilityFilters } from "./utils";

export const List = styled.ul`
  list-style: none;
  padding-inline-start: 0;
  width: 100%;
  li:not(:last-child) {
    border-bottom: 1px solid black;
  }
`;

export const ListItem = styled.li`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 1rem;
  padding-bottom: 1rem;
`;

export const ComicBookTitle = styled.span`
  ${props => props.read && "text-decoration: line-through;"}
`;

export const Filters = ({
  visibilityFilter,
  onVisibilityFilterChange,
  allCount,
  readsCount,
  pendingCount
}) => (
  <FilterList style={{ width: "100%" }} marginTop="1rem">
    <FilterList.Item
      selected={visibilityFilter === VisibilityFilters.ALL}
      onClick={() => onVisibilityFilterChange(VisibilityFilters.ALL)}
    >
      All
      <span title="results" class="count">
        {allCount}
      </span>
    </FilterList.Item>
    <FilterList.Item
      selected={visibilityFilter === VisibilityFilters.READS}
      onClick={() => onVisibilityFilterChange(VisibilityFilters.READS)}
    >
      <span title="results" class="count">
        {readsCount}
      </span>
      Reads
    </FilterList.Item>
    <FilterList.Item
      selected={visibilityFilter === VisibilityFilters.PENDING}
      onClick={() => onVisibilityFilterChange(VisibilityFilters.PENDING)}
    >
      <span title="results" class="count">
        {pendingCount}
      </span>
      Pending
    </FilterList.Item>
  </FilterList>
);

export const Container = ({ children }) => (
  <BaseStyles>
    <Flex flexDirection="column" alignItems="center" margin="2rem">
      {children}
    </Flex>
  </BaseStyles>
);
