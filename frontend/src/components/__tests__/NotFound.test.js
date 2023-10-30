import React from "react";
import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import NotFound from "../NotFound";

describe("NotFound Component", () => {
  test("renders the not found message", () => {
    render(
      <MemoryRouter>
        <NotFound />
      </MemoryRouter>,
    );

    // Check if the not found message is displayed
    const messageElement = screen.getByText(
      "404 Error. Page Not Found",
    );
    expect(messageElement).toBeInTheDocument();
  });

  test("renders the 'Return Home' button", () => {
    render(
      <MemoryRouter>
        <NotFound />
      </MemoryRouter>,
    );

    // Check if the 'Back Home' button is displayed and has the correct link
    const buttonElement = screen.getByText("Return Home");
    expect(buttonElement).toBeInTheDocument();
    expect(buttonElement).toHaveAttribute("href", "/");
  });

  test("renders the not found image", () => {
    render(
      <MemoryRouter>
        <NotFound />
      </MemoryRouter>,
    );

    // Check if the not found image is displayed
    const imageElement = screen.getByRole("img");
    expect(imageElement).toBeInTheDocument();
    expect(imageElement).toHaveAttribute(
      "alt",
      "404 Error. Page Not Found",
    );
  });
});
