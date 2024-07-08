# CHANGELOG

## v2.10.0 (2024-07-08)

### Feature

* feat: add yield table for tree type Pin Negru (#58)

Co-authored-by: Maxim &lt;maxim@MacBook-Pro-von-Maxim.local&gt; ([`cc42e6c`](https://github.com/treely/openyieldtables/commit/cc42e6cb28ece30c86f666b0decc4510a4aa8a90))

## v2.9.0 (2024-07-08)

### Feature

* feat: add yield table for tree type Salcie din Samanta (#57)

Co-authored-by: Maxim &lt;maxim@MacBook-Pro-von-Maxim.local&gt; ([`7a7ba43`](https://github.com/treely/openyieldtables/commit/7a7ba43e3f5d51d520e673b087106fefd57a5b10))

## v2.8.0 (2024-07-08)

### Feature

* feat: add yield table for tree type Plop alb si Plop negru (#56)

Co-authored-by: Maxim &lt;maxim@MacBook-Pro-von-Maxim.local&gt; ([`5ac83cd`](https://github.com/treely/openyieldtables/commit/5ac83cd54c989d195959a76aaf7de381cdb1d746))

## v2.7.0 (2024-07-08)

### Feature

* feat: add yield table for tree type Mesteacan (#55)

Co-authored-by: Maxim &lt;maxim@MacBook-Pro-von-Maxim.local&gt; ([`876f44d`](https://github.com/treely/openyieldtables/commit/876f44d7a52229798ffeb537acc3f07738ba1653))

## v2.6.0 (2024-07-08)

### Feature

* feat: add yield table for tree type Fag din samanta (#54)

Co-authored-by: Maxim &lt;maxim@MacBook-Pro-von-Maxim.local&gt; ([`e23f0f7`](https://github.com/treely/openyieldtables/commit/e23f0f7e8bfbaec62279cf7575e62fd4725491da))

### Unknown

* Add translations to roadmap ([`1395bcb`](https://github.com/treely/openyieldtables/commit/1395bcb1de22e94dd7f410b189ddd117371bef3c))

## v2.5.0 (2024-07-05)

### Feature

* feat: add yield table for tree type Pin Silvestru (#53)

Co-authored-by: Maxim &lt;maxim@MacBook-Pro-von-Maxim.local&gt; ([`148237b`](https://github.com/treely/openyieldtables/commit/148237b2f885b50629d7e9021fa816680d99e0ea))

## v2.4.0 (2024-07-05)

### Documentation

* docs: Fix typo in yield table explorer ([`dbb9598`](https://github.com/treely/openyieldtables/commit/dbb95985e422761559a1da8af9a046b55bb1cd05))

### Feature

* feat: add yield table for tree type Larice (#63)

Co-authored-by: Maxim &lt;maxim@MacBook-Pro-von-Maxim.local&gt; ([`abb5e52`](https://github.com/treely/openyieldtables/commit/abb5e526b4b5c04697546b1eb3f6bae4297db0ad))

### Test

* test: Remove length assertion from api test ([`e2085c7`](https://github.com/treely/openyieldtables/commit/e2085c74eaee05f692ec4ad459cc6ac2101ad348))

* test: Remove length assertion in test (#59) ([`28fb8dd`](https://github.com/treely/openyieldtables/commit/28fb8ddd850b330a116abee5f17da327b939a74e))

## v2.3.0 (2024-06-26)

### Documentation

* docs: Add a roadmap ([`81744dd`](https://github.com/treely/openyieldtables/commit/81744dd1cec5a3abbdd765d48a5d97dded3dc45f))

* docs: Change GmbH to FlexCo ([`22f7035`](https://github.com/treely/openyieldtables/commit/22f70352bdae706ac80c6268f2c55da9eb30c606))

### Feature

* feat: Add tree type to meta data

The tree type can either be `coniferous` or `deciduous`. ([`e5fe129`](https://github.com/treely/openyieldtables/commit/e5fe129660c3d779ae46a3aced1d49e19091d293))

## v2.2.2 (2024-05-22)

### Fix

* fix: Fix age level for yield table 11 ([`3cb56d6`](https://github.com/treely/openyieldtables/commit/3cb56d6ec98e242b4c690d52cc61172aa3ea0e7c))

## v2.2.1 (2024-05-08)

### Documentation

* docs: Add header to yield table explorer ([`05703c4`](https://github.com/treely/openyieldtables/commit/05703c4f6764019201f4ec6f44ed9dd1c1e34b75))

### Fix

* fix: Remove TimberControl Database as source ([`963aed0`](https://github.com/treely/openyieldtables/commit/963aed0d334cfb19d62be0b1412d8eab2ea53153))

## v2.2.0 (2024-05-02)

### Documentation

* docs: Add HTML responses to API ([`bfa66e1`](https://github.com/treely/openyieldtables/commit/bfa66e153611fada69a18adb9f50eeb2063023ea))

* docs: Correct company name (#42) ([`37d9a33`](https://github.com/treely/openyieldtables/commit/37d9a33c77f2392e1e2f9cacda9845bf87399509))

### Feature

* feat: Update sources in meta data ([`923daea`](https://github.com/treely/openyieldtables/commit/923daea57aba20543a96d05931ab3f7dec67d5d6))

## v2.1.0 (2024-04-24)

### Feature

* feat(data): Add Lockow Birch yield table ([`1a88c60`](https://github.com/treely/openyieldtables/commit/1a88c608d0634b63195338d810392c9f1ed865fa))

## v2.0.0 (2024-04-24)

### Breaking

* fix: Remove duplicate yield tables from data

BREAKING CHANGE: Remove duplicate yield tables from data

The yield tables with ID 95, 96, 97 and 98 are removed,
because they are duplicates of the yield tables with ID
88, 89, 90 and 91. ([`b3bf908`](https://github.com/treely/openyieldtables/commit/b3bf908d8604f7f1b3d9d00b6aa72f96f85c4857))

## v1.0.0 (2024-04-23)

### Breaking

* feat: Rename get_yield_table_data function

BREAKING CHANGE: Rename get_yield_table_data function

To be consistent the get_yield_table_data function is
renamed to get_yield_table since the function returns
the full YieldTable and not only the data. Additionally,
the YieldTable model has been updated to contain an
object of data instead an array of data since the array
always only contained one entry. ([`f7f1742`](https://github.com/treely/openyieldtables/commit/f7f1742dba8a139235d6f80607c92a0ec5514e17))

### Build

* build: Set up cross origin resource sharing ([`b598b3f`](https://github.com/treely/openyieldtables/commit/b598b3fca05ccfd9c51ce04729a39c2681e64c6d))

### Ci

* ci: Build package in test workflow ([`2a4a396`](https://github.com/treely/openyieldtables/commit/2a4a3962cce730b16e6731f5e782c7918f29847a))

### Documentation

* docs: Fix getting started ([`101001d`](https://github.com/treely/openyieldtables/commit/101001dd0671a5531e5bded8643b6144643147b5))

* docs: Update start page ([`55bdc16`](https://github.com/treely/openyieldtables/commit/55bdc166cb87b5bd6632fcb2ef1d232cdec10d2a))

* docs: Update the company type of Tree.ly in the license ([`6eb999e`](https://github.com/treely/openyieldtables/commit/6eb999e231e74cd70f00459ab146f4ed2c735c03))

* docs: Remove routes from API index page ([`2740822`](https://github.com/treely/openyieldtables/commit/2740822553b66c4931021ddefd3ef50c93ea9c65))

* docs: Add link to PyPI in documentation ([`e0ed0b9`](https://github.com/treely/openyieldtables/commit/e0ed0b9bb6c7703d9e7180c94e1c7ac75d0f41cd))

* docs: Add index page for api ([`d24d826`](https://github.com/treely/openyieldtables/commit/d24d8263c69a638c9f7b67f9ab32f60172455998))

* docs: Add project meta data ([`9883f5a`](https://github.com/treely/openyieldtables/commit/9883f5a756797ae60a6772871b442932a4f4535b))

* docs: Use absolute link in README in order to work on PyPI ([`14d15f0`](https://github.com/treely/openyieldtables/commit/14d15f09e038326345e15ca950c06a7f9b0d9ebd))

* docs: Add badges to the README.md and add license to pyproject.toml ([`1faa9ce`](https://github.com/treely/openyieldtables/commit/1faa9ceb240c7ce228ad2d9247e23248b34cda4e))

* docs: Add Readthedocs badge to readme ([`f861ab0`](https://github.com/treely/openyieldtables/commit/f861ab0caace17b0d08cfe16abfb8ac824e8e21c))

* docs: Setup Readthedocs deploy ([`fa95be7`](https://github.com/treely/openyieldtables/commit/fa95be789a271e4655b86755df4c322ea43349d6))

* docs: Fix broken link in readme ([`ff01189`](https://github.com/treely/openyieldtables/commit/ff01189d88b869eaa8158c5b756b389f37b5138c))

## v0.0.0 (2024-04-18)

### Build

* build: Use COMMIT_TOKEN in release workflow ([`bcd206c`](https://github.com/treely/openyieldtables/commit/bcd206ca960ad16fd2c4b2bd09021cb99f064079))

* build: Remove version ([`8c74dc0`](https://github.com/treely/openyieldtables/commit/8c74dc0854a81ee78dc89c1f3529acc3be888fd5))

* build: Setup release workflow ([`0dcb65b`](https://github.com/treely/openyieldtables/commit/0dcb65b9a645452b3a0c50457567600dc868baf6))

### Unknown

* Push an image to ECR only on pushes to the main branch ([`b3ef293`](https://github.com/treely/openyieldtables/commit/b3ef293087f6f9ec41fd152fbed862ad6ef052b5))

* Update yield table fields ([`58c99a7`](https://github.com/treely/openyieldtables/commit/58c99a7d1938a110e81914ae8490ba431ac9a2ee))

* Add Tree.ly yield tables ([`427207e`](https://github.com/treely/openyieldtables/commit/427207e30a03ae48b5298afdb2197f4cd7ca6fe4))

* Fix contribution guideline link in the readme ([`8b2b3af`](https://github.com/treely/openyieldtables/commit/8b2b3af18ea691fd197cae0c697a8c855df143de))

* Update the contribution docs and add Docker documentation ([`f39c45e`](https://github.com/treely/openyieldtables/commit/f39c45e3a8c4fefab631a10ba43e8c0d8e9e446a))

* Fix Dockerfile to contain the openyieldtables module ([`8976113`](https://github.com/treely/openyieldtables/commit/8976113944d250ad2aa569013359f572798c3e4d))

* Add readiness and liveness endpoints ([`cac21d8`](https://github.com/treely/openyieldtables/commit/cac21d8d24736d5534bfb7b5278a3b5b6425ee76))

* Setup docker image ([`4264759`](https://github.com/treely/openyieldtables/commit/4264759339f66e101f86ab0da821070c793edb5b))

* Setup api ([`6fded29`](https://github.com/treely/openyieldtables/commit/6fded2905c432b951766e9d315fc72afe7511449))

* Setup documentation with mkdocs ([`d366c9c`](https://github.com/treely/openyieldtables/commit/d366c9c64af656f93113600cde96acedc7f50644))

* Move data and models dir to src ([`eef076f`](https://github.com/treely/openyieldtables/commit/eef076f6ffb2385640e747a09353c509b478a5c8))

* Clean yield_tables_meta.csv ([`47adbbf`](https://github.com/treely/openyieldtables/commit/47adbbfbf1ed87616c31699fa9d5ff7872282b1f))

* Implement functions to get yield table (meta)data ([`9768f0d`](https://github.com/treely/openyieldtables/commit/9768f0d2fdaa549aa0a5551049df1085e6d68361))

* Add github workflow ([`c8f37f7`](https://github.com/treely/openyieldtables/commit/c8f37f72b4c536a68e80af574e6895bf58ff2eea))

* Add static type checking ([`b941d10`](https://github.com/treely/openyieldtables/commit/b941d10872b7604cad08caa03c9e4462773e7d8e))

* Setup testing and linting ([`735d8ff`](https://github.com/treely/openyieldtables/commit/735d8ff897ee6db358434b4acba7d7e731a2119c))

* Setup poetry ([`1c89f5c`](https://github.com/treely/openyieldtables/commit/1c89f5c792e14f65737fe34f470f3def56fd2672))

* Add .gitignore ([`bbbccb9`](https://github.com/treely/openyieldtables/commit/bbbccb9ff6728a650a16df1e38f872d3537d062f))

* first commit ([`1581adf`](https://github.com/treely/openyieldtables/commit/1581adf9e6ea67fd114917c7e7c9eda2aa4016db))
