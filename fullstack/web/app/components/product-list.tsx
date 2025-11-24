"use client";

import { useInfiniteQuery } from "@tanstack/react-query";
import { Product } from "@/app/types";
import ProductCard from "./product-card";
import { useEffect } from "react";
import { useInView } from "react-intersection-observer";

const fetchProducts = async ({ pageParam = 0 }) => {
  const res = await fetch(
    `http://localhost:8000/api/v1/products?skip=${pageParam}&limit=10`
  );
  if (!res.ok) {
    throw new Error("Network response was not ok");
  }
  const data = await res.json();
  return data;
};

export default function ProductList() {
  const {
    data,
    error,
    fetchNextPage,
    hasNextPage,
    isFetching,
    isFetchingNextPage,
    status,
  } = useInfiniteQuery({
    queryKey: ["products"],
    queryFn: fetchProducts,
    getNextPageParam: (lastPage, allPages) => {
      const nextPage = allPages.length * 10;
      return lastPage.length === 10 ? nextPage : undefined;
    },
  });

  const { ref, inView } = useInView();

  useEffect(() => {
    if (inView && hasNextPage) {
      fetchNextPage();
    }
  }, [inView, hasNextPage, fetchNextPage]);

  if (status === "pending") {
    return <p>Loading...</p>;
  }

  if (status === "error") {
    return <p>Error: {error.message}</p>;
  }

  return (
    <div>
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3">
        {data.pages.map((page) =>
          page.map((product: Product) => (
            <ProductCard key={product.id} product={product} />
          ))
        )}
      </div>
      <div ref={ref}>
        {isFetchingNextPage
          ? "Loading more..."
          : hasNextPage
          ? "Load More"
          : "Nothing more to load"}
      </div>
    </div>
  );
}
