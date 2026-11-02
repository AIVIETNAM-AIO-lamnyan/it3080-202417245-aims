# Changelog

All notable changes to this project are documented in this file.

## [Unreleased]

## [1.1.0] - 2026-11-03

### Added

- Cart sorting by DVD title or cost.
- Search DVDs by category.

## [1.0.0] - 2026-11-03

### Added

- `Cart.print_cart()` to display the DVDs in a cart.
- `search_by_title()` to find DVDs by title.
- `Cart.total_cost_with_discount()` to calculate discounted totals.
- AIMS package structure, pull request template, and use-case documentation.

### Fixed

- Reject DVDs once the cart reaches its 20-item limit.
- Apply discounts to the remaining total and reject percentages outside 0–100.

### Changed

- Display cart-add confirmations in Vietnamese and include the DVD title.
- Demonstrate cart printing and title search in the command-line app.
