#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: 250a666
#
Name     : R-data.tree
Version  : 1.1.0
Release  : 10
URL      : https://cran.r-project.org/src/contrib/data.tree_1.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/data.tree_1.1.0.tar.gz
Summary  : General Purpose Hierarchical Data Structure
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-R6
Requires: R-stringi
BuildRequires : R-R6
BuildRequires : R-igraph
BuildRequires : R-stringi
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
tree in various orders. Aggregate, cumulate, print, plot, convert to and from
    data.frame and more. Useful for decision trees, machine learning, finance,
    conversion from and to JSON, and many other applications.

%prep
%setup -q -n data.tree
pushd ..
cp -a data.tree buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1699900811

%install
export SOURCE_DATE_EPOCH=1699900811
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/data.tree/DESCRIPTION
/usr/lib64/R/library/data.tree/INDEX
/usr/lib64/R/library/data.tree/Meta/Rd.rds
/usr/lib64/R/library/data.tree/Meta/data.rds
/usr/lib64/R/library/data.tree/Meta/features.rds
/usr/lib64/R/library/data.tree/Meta/hsearch.rds
/usr/lib64/R/library/data.tree/Meta/links.rds
/usr/lib64/R/library/data.tree/Meta/nsInfo.rds
/usr/lib64/R/library/data.tree/Meta/package.rds
/usr/lib64/R/library/data.tree/Meta/vignette.rds
/usr/lib64/R/library/data.tree/NAMESPACE
/usr/lib64/R/library/data.tree/NEWS
/usr/lib64/R/library/data.tree/R/data.tree
/usr/lib64/R/library/data.tree/R/data.tree.rdb
/usr/lib64/R/library/data.tree/R/data.tree.rdx
/usr/lib64/R/library/data.tree/data/acme.rda
/usr/lib64/R/library/data.tree/data/mushroom.rda
/usr/lib64/R/library/data.tree/doc/applications.R
/usr/lib64/R/library/data.tree/doc/applications.Rmd
/usr/lib64/R/library/data.tree/doc/applications.html
/usr/lib64/R/library/data.tree/doc/data.tree.R
/usr/lib64/R/library/data.tree/doc/data.tree.Rmd
/usr/lib64/R/library/data.tree/doc/data.tree.html
/usr/lib64/R/library/data.tree/doc/index.html
/usr/lib64/R/library/data.tree/extdata/flare.json
/usr/lib64/R/library/data.tree/extdata/jennylind.yaml
/usr/lib64/R/library/data.tree/extdata/portfolio.csv
/usr/lib64/R/library/data.tree/extdata/useR15.csv
/usr/lib64/R/library/data.tree/help/AnIndex
/usr/lib64/R/library/data.tree/help/aliases.rds
/usr/lib64/R/library/data.tree/help/data.tree.rdb
/usr/lib64/R/library/data.tree/help/data.tree.rdx
/usr/lib64/R/library/data.tree/help/paths.rds
/usr/lib64/R/library/data.tree/html/00Index.html
/usr/lib64/R/library/data.tree/html/R.css
/usr/lib64/R/library/data.tree/tests/testthat.R
/usr/lib64/R/library/data.tree/tests/testthat/test-draw.R
/usr/lib64/R/library/data.tree/tests/testthat/test-treeConstruction.R
/usr/lib64/R/library/data.tree/tests/testthat/test-treeConversionApe.R
/usr/lib64/R/library/data.tree/tests/testthat/test-treeConversionDataFrame.R
/usr/lib64/R/library/data.tree/tests/testthat/test-treeConversionDendrogram.R
/usr/lib64/R/library/data.tree/tests/testthat/test-treeConversionList.R
/usr/lib64/R/library/data.tree/tests/testthat/test-treeConversionParty.R
/usr/lib64/R/library/data.tree/tests/testthat/test-treeConversionRpart.R
/usr/lib64/R/library/data.tree/tests/testthat/test-treeConversionigraph.R
/usr/lib64/R/library/data.tree/tests/testthat/test-treeDocu.R
/usr/lib64/R/library/data.tree/tests/testthat/test-treeMethods.R
/usr/lib64/R/library/data.tree/tests/testthat/test-treeMethodsSideEffect.R
/usr/lib64/R/library/data.tree/tests/testthat/test-util.R
