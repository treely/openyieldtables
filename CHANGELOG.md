# CHANGELOG



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
