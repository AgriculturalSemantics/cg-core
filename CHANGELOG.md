# 2023-09-12

- Archive v2.0.0 docs to `docs/v2.0.0` so we have a historical reference
- Update IPtypes.csv and add script to parse and generate IPtypes.html

# 2023-09-11

- Re-organize project
  - Data like CSV and RDF into `data` directory
  - User-facing content into `docs` directory
- Update dependencies in line with Bootstrap v5.3.x

# 2022-11-04

- Update Bootstrap from v4.6 to v5.2

# 2021-01-19

- Fix links to xCoord, yCoord, and code in docs
- Remove unnecessary links in docs
- Update to Bootstrap v4.6.0

# 2021-01-05

- Use sass instead of node-sass (sass is the only officially maintained version)

# 2020-11-15

- Use node-sass 5.0.0

# 2020-10-19

- Update Bootstrap from 4.5.0 to 4.5.3

# 2020-07-27

- Use JavaScript from local project instead of a CDN

# 2020-07-26

- Update Bootstrap from 4.4.1 to 4.5.0
- Update Node.js dependencies
- cgcore.html:
  - sort metadata classes alphabetically
  - don't use uppercase for class names (except ScientificPublication, because that one is custom and I should consult Marie and update all the examples)

# 2020-07-21

- Adjust look and feel of cgcore.html:
  - Use Bootstrap classes to set the width of table cells instead of using CSS `width` directly
  - Vertically center the property and class badges in tables
  - Add Bootstrap "scrollspy" to left sidebar to replace old "quick jump" indicate progress
  - Use HTML lists for examples when there are multiple values

TODO:

- Spelling and grammar
