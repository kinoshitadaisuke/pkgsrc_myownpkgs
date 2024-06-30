# $NetBSD$

DISTNAME=	astropy-6.1.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/astropy/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://www.astropy.org/
COMMENT=	Python module for astronomical calculations and data analysis
LICENSE=	modified-bsd

DEPENDS+=	flatbuffers>=23.5.26:../../pkgsrc_myownpkgs/flatbuffers
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.21.0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-pyerfa>=2.0:../../pkgsrc_myownpkgs/py-pyerfa
DEPENDS+=	${PYPKGPREFIX}-yaml>=3.13:../../textproc/py-yaml
DEPENDS+=	${PYPKGPREFIX}-packaging>=19.0:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-scipy>=1.5:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=3.3:../../graphics/py-matplotlib
DEPENDS+=	${PYPKGPREFIX}-h5py>=2.9.0:../../devel/py-h5py
DEPENDS+=	${PYPKGPREFIX}-beautifulsoup4>=4.9.3:../../www/py-beautifulsoup4
DEPENDS+=	${PYPKGPREFIX}-html5lib>=1.0.1:../../textproc/py-html5lib
DEPENDS+=	${PYPKGPREFIX}-bleach>=3.2.1:../../www/py-bleach
DEPENDS+=	libxml2>=2.9.10:../../textproc/libxml2
DEPENDS+=	${PYPKGPREFIX}-pandas>=0.14:../../math/py-pandas

DEPENDS+=	${PYPKGPREFIX}-sortedcontainers>=2.2.2:../../devel/py-sortedcontainers
DEPENDS+=	${PYPKGPREFIX}-pytz>=2020.4:../../time/py-pytz
DEPENDS+=	${PYPKGPREFIX}-setuptools>=50.3.2:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=6.2:../../devel/py-setuptools_scm
DEPENDS+=	${PYPKGPREFIX}-mpmath>=1.1.0:../../math/py-mpmath
DEPENDS+=	${PYPKGPREFIX}-asdf>=2.12.0:../../math/py-asdf
DEPENDS+=	${PYPKGPREFIX}-bottleneck>=1.3.2:../../math/py-bottleneck
DEPENDS+=	${PYPKGPREFIX}-certifi>0:../../security/py-certifi
DEPENDS+=	${PYPKGPREFIX}-extension-helpers>=0.1:../../devel/py-extension-helpers
DEPENDS+=	${PYPKGPREFIX}-jplephem>=2.15:../../pkgsrc_myownpkgs/py-jplephem
DEPENDS+=	${PYPKGPREFIX}-colorlog>=6.6.0:../../devel/py-colorlog
DEPENDS+=	${PYPKGPREFIX}-wheel>0:../../devel/py-wheel
DEPENDS+=	${PYPKGPREFIX}-cython>=0.29.34:../../devel/py-cython
#DEPENDS+=	${PYPKGPREFIX}-dask>=0:../../wip/py-dask
#DEPENDS+=	${PYPKGPREFIX}-arrow>=0:../../time/py-arrow
DEPENDS+=	${PYPKGPREFIX}-asdf-astropy>=0.3:../../pkgsrc_myownpkgs/py-asdf-astropy
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=3.10.0.1:../../devel/py-typing-extensions
DEPENDS+=	${PYPKGPREFIX}-fsspec>=2022.8.2:../../sysutils/py-fsspec
DEPENDS+=	${PYPKGPREFIX}-s3fs>=2022.8.2:../../pkgsrc_myownpkgs/py-s3fs
DEPENDS+=	${PYPKGPREFIX}-pre-commit>=0:../../wip/py-pre-commit
DEPENDS+=	${PYPKGPREFIX}-sphinx>=0:../../textproc/py-sphinx
DEPENDS+=	${PYPKGPREFIX}-sphinx-astropy>=1.6:../../textproc/py-sphinx-astropy
DEPENDS+=	${PYPKGPREFIX}-jinja2>=3.0:../../textproc/py-jinja2

TEST_DEPENDS+=	${PYPKGPREFIX}-test>=7.0:../../devel/py-test
TEST_DEPENDS+=	${PYPKGPREFIX}-test-doctestplus>=0.12:../../devel/py-test-doctestplus
TEST_DEPENDS+=	${PYPKGPREFIX}-test-astropy-header>=0.2.1:../../pkgsrc_myownpkgs/py-test-astropy-header
TEST_DEPENDS+=	${PYPKGPREFIX}-test-astropy>=0.10:../../pkgsrc_myownpkgs/py-test-astropy
TEST_DEPENDS+=	${PYPKGPREFIX}-test-xdist>=0:../../devel/py-test-xdist
TEST_DEPENDS+=	${PYPKGPREFIX}-objgraph>=0:../../graphics/py-objgraph
TEST_DEPENDS+=	${PYPKGPREFIX}-ipython>=4.2:../../devel/py-ipython
TEST_DEPENDS+=	${PYPKGPREFIX}-coverage>=0:../../devel/py-coverage
TEST_DEPENDS+=	${PYPKGPREFIX}-skyfield>=1.20:../../pkgsrc_myownpkgs/py-skyfield
TEST_DEPENDS+=	${PYPKGPREFIX}-sgp4>=2.3:../../pkgsrc_myownpkgs/py-sgp4

PYTHON_VERSIONS_INCOMPATIBLE=	27 37 38
USE_PKG_RESOURCES=		yes
USE_LANGUAGES=			c c++

post-install:
	cd ${DESTDIR}${PREFIX}/bin && \
	(${MV} fits2bitmap fits2bitmap-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} fitscheck fitscheck-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} fitsdiff fitsdiff-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} fitsheader fitsheader-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} fitsinfo fitsinfo-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} samp_hub samp_hub-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} showtable showtable-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} volint volint-${PYVERSSUFFIX} || ${TRUE}; \
	${MV} wcslint wcslint-${PYVERSSUFFIX} || ${TRUE};)


.include "../../lang/python/egg.mk"
.include "../../math/py-numpy/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
