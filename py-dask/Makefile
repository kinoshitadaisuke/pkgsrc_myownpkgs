# $NetBSD$

DISTNAME=	dask-2025.12.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=d/dask/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/dask/dask/
COMMENT=	Flexible parallel computing library for analytics
LICENSE=	modified-bsd

.include "../../mk/bsd.prefs.mk"
.include "../../lang/python/pyversion.mk"

# build dependencies
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=80:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=9:../../devel/py-setuptools_scm
TOOL_DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel
TOOL_DEPENDS+=	${PYPKGPREFIX}-versioneer>=0.28:../../devel/py-versioneer
# dependencies
DEPENDS+=	${PYPKGPREFIX}-click>=8.1:../../devel/py-click
DEPENDS+=	${PYPKGPREFIX}-cloudpickle>=3.0.0:../../converters/py-cloudpickle
DEPENDS+=	${PYPKGPREFIX}-fsspec>=2021.09.0:../../sysutils/py-fsspec
DEPENDS+=	${PYPKGPREFIX}-packaging>=20.0:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-partd>=1.4.0:../../pkgsrc_myownpkgs/py-partd
DEPENDS+=	${PYPKGPREFIX}-yaml>=5.3.1:../../textproc/py-yaml
DEPENDS+=	${PYPKGPREFIX}-toolz>=0.12.0:../../devel/py-toolz
DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>=4.13.0:../../devel/py-importlib-metadata
# optional dependencies
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.24:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-pandas>=2.0:../../math/py-pandas
DEPENDS+=	${PYPKGPREFIX}-apache-arrow>=14.0.1:../../pkgsrc_myownpkgs/py-apache-arrow
DEPENDS+=	${PYPKGPREFIX}-distributed>=2025.12.0:../../pkgsrc_myownpkgs/py-distributed
DEPENDS+=	${PYPKGPREFIX}-bokeh>=3.1.0:../../wip/py-bokeh
DEPENDS+=	${PYPKGPREFIX}-jinja2>=2.10.3:../../textproc/py-jinja2
DEPENDS+=	${PYPKGPREFIX}-lz4>=4.3.2:../../archivers/py-lz4

DEPENDS+=	${PYPKGPREFIX}-cytoolz-[0-9]*:../../devel/py-cytoolz
DEPENDS+=	${PYPKGPREFIX}-h5py>=2.10:../../devel/py-h5py
DEPENDS+=	${PYPKGPREFIX}-mmh3>=2.5.1:../../devel/py-mmh3
DEPENDS+=	${PYPKGPREFIX}-snappy>=0.5.4:../../devel/py-snappy
DEPENDS+=	${PYPKGPREFIX}-sqlalchemy-[0-9]*:../../databases/py-sqlalchemy
DEPENDS+=	${PYPKGPREFIX}-graphviz-[0-9]*:../../graphics/py-graphviz
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=3.4.1:../../graphics/py-matplotlib
DEPENDS+=	${PYPKGPREFIX}-xarray-[0-9]*:../../math/py-xarray
DEPENDS+=	${PYPKGPREFIX}-scikit-image-[0-9]*:../../math/py-scikit-image
DEPENDS+=	${PYPKGPREFIX}-scipy-[0-9]*:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-psutil-[0-9]*:../../sysutils/py-psutil
.if  ${PYTHON_VERSION} < 313
DEPENDS+=	${PYPKGPREFIX}-cityhash-[0-9]*:../../wip/py-cityhash
.endif
#DEPENDS+=	${PYPKGPREFIX}-dask_expr>=1.1.17:../../wip/py-dask_expr
DEPENDS+=	${PYPKGPREFIX}-fastavro>=1.1.0:../../wip/py-fastavro
DEPENDS+=	${PYPKGPREFIX}-tblib>=1.6.0:../../wip/py-tblib
DEPENDS+=	${PYPKGPREFIX}-zict>=2.1.0:../../wip/py-zict

TEST_DEPENDS+=	${PYPKGPREFIX}-test-[0-9]*:../../devel/py-test
TEST_DEPENDS+=	${PYPKGPREFIX}-test-cov-[0-9]*:../../devel/py-test-cov
TEST_DEPENDS+=	${PYPKGPREFIX}-test-rerunfailures-[0-9]*:../../devel/py-test-rerunfailures
TEST_DEPENDS+=	${PYPKGPREFIX}-test-timeout-[0-9]*:../../devel/py-test-timeout
TEST_DEPENDS+=	${PYPKGPREFIX}-test-xdist-[0-9]*:../../devel/py-test-xdist
TEST_DEPENDS+=	${PYPKGPREFIX}-multipledispatch>=0.6.0:../../devel/py-multipledispatch
TEST_DEPENDS+=	${PYPKGPREFIX}-tables>=3.9:../../math/py-tables
TEST_DEPENDS+=	${PYPKGPREFIX}-numexpr>=2.9.0:../../math/py-numexpr
TEST_DEPENDS+=	${PYPKGPREFIX}-pre-commit-[0-9]*:../../wip/py-pre-commit
# TODO: Get These Working
# TEST_DEPENDS+=	${PYPKGPREFIX}-aiohttp>=3.9.5:../../www/py-aiohttp
# TEST_DEPENDS+=	${PYPKGPREFIX}-s3fs>=2022*:../../wip/py-s3fs
# TEST_DEPENDS+=	${PYPKGPREFIX}-sparse>=0.11.2:../../wip/py-sparse

# The setup.py has integration with pytest-runner, but throws odd errors
do-test:
	cd ${WRKSRC} && ${SETENV} ${TEST_ENV} ${PYTHONBIN} -m pytest -s --full-trace

post-install:
	cd ${DESTDIR}${PREFIX}/bin && ${MV} dask dask-${PYVERSSUFFIX}

USE_LANGUAGES=	# none

.include "../../lang/python/wheel.mk"
.include "../../math/py-numpy/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
