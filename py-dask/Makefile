# $NetBSD$

DISTNAME=	dask-2023.4.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=d/dask/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/dask/
COMMENT=	Flexible parallel computing library for analytics
LICENSE=	modified-bsd

BUILD_DEPENDS+=       ${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel

DEPENDS+=	${PYPKGPREFIX}-setuptools>=62.6:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-versioneer>=0.28:../../wip/py-versioneer
DEPENDS+=	${PYPKGPREFIX}-click>=8.0:../../devel/py-click
DEPENDS+=	${PYPKGPREFIX}-cloudpickle>=1.5.1:../../wip/py-cloudpickle
DEPENDS+=	${PYPKGPREFIX}-fsspec>=2021.09.0:../../sysutils/py-fsspec
DEPENDS+=	${PYPKGPREFIX}-packaging>=20.0:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-partd>=1.2.0:../../wip/py-partd
DEPENDS+=	${PYPKGPREFIX}-yaml>=5.3.1:../../textproc/py-yaml
DEPENDS+=	${PYPKGPREFIX}-toolz>=0.10.0:../../devel/py-toolz
DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>=4.13.0:../../pkgsrc_myownpkgs/py-importlib-metadata
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.21:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-pandas>=1.3:../../math/py-pandas
DEPENDS+=	${PYPKGPREFIX}-distributed>=2023.4.1:../../pkgsrc_myownpkgs/py-distributed
DEPENDS+=	${PYPKGPREFIX}-bokeh>=2.4.2:../../wip/py-bokeh
DEPENDS+=	${PYPKGPREFIX}-jinja2>2.10.3:../../textproc/py-jinja2
DEPENDS+=	${PYPKGPREFIX}-zict>=2.1.0:../../wip/py-zict

TEST_DEPENDS+=	${PYPKGPREFIX}-test-[0-9]*:../../devel/py-test
TEST_DEPENDS+=	${PYPKGPREFIX}-test-rerunfailures-[0-9]*:../../devel/py-test-rerunfailures
TEST_DEPENDS+=	${PYPKGPREFIX}-test-xdist-[0-9]*:../../devel/py-test-xdist
TEST_DEPENDS+=	${PYPKGPREFIX}-multipledispatch>=0.6.0*:../../devel/py-multipledispatch
TEST_DEPENDS+=	${PYPKGPREFIX}-pre-commit-[0-9]*:../../wip/py-pre-commit
# TEST_DEPENDS+=	${PYPKGPREFIX}-s3fs>=2022*:../../wip/py-s3fs
# TEST_DEPENDS+=	${PYPKGPREFIX}-sparse>=0.11.2:../../wip/py-sparse

# The setup.py has integration with pytest-runner, but throws odd errors
do-test:
	cd ${WRKSRC} && ${SETENV} ${TEST_ENV} ${PYTHONBIN} -m pytest -s

post-install:
	cd ${DESTDIR}${PREFIX}/bin && ${MV} dask dask-${PYVERSSUFFIX}

USE_LANGUAGES=	# none

.include "../../mk/bsd.prefs.mk"
.include "options.mk"
.include "../../lang/python/wheel.mk"
.include "../../math/py-numpy/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
