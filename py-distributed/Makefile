# $NetBSD$

DISTNAME=	distributed-2025.2.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel net
GITHUB_PROJECT=	distributed
MASTER_SITES=	${MASTER_SITE_GITHUB:=dask/}


MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/dask/distributed/
COMMENT=	Distributed is the parallel scheduler for dask
LICENSE=	modified-bsd

BUILD_DEPENDS+=       ${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel

DEPENDS+=	${PYPKGPREFIX}-click>=8.1.3:../../devel/py-click
DEPENDS+=	${PYPKGPREFIX}-sortedcontainers>=2.0.1:../../devel/py-sortedcontainers
DEPENDS+=	${PYPKGPREFIX}-cloudpickle>=2.2.0:../../converters/py-cloudpickle
DEPENDS+=	${PYPKGPREFIX}-jinja2-[0-9]*:../../textproc/py-jinja2
DEPENDS+=	${PYPKGPREFIX}-msgpack-[0-9]*:../../devel/py-msgpack
DEPENDS+=	${PYPKGPREFIX}-psutil>=5.0:../../sysutils/py-psutil
DEPENDS+=	${PYPKGPREFIX}-toolz>=0.8.2:../../devel/py-toolz
DEPENDS+=	${PYPKGPREFIX}-tornado>=6.0.3:../../www/py-tornado
DEPENDS+=	${PYPKGPREFIX}-tblib>=1.7.0:../../wip/py-tblib

TEST_DEPENDS+=	${PYPKGPREFIX}-lz4>=3.1.10:../../archivers/py-lz4
TEST_DEPENDS+=	${PYPKGPREFIX}-zstandard>=0.18.0:../../archivers/py-zstandard
TEST_DEPENDS+=	${PYPKGPREFIX}-requests>=2.28.1:../../devel/py-requests
TEST_DEPENDS+=	${PYPKGPREFIX}-test-[0-9]*:../../devel/py-test
TEST_DEPENDS+=	${PYPKGPREFIX}-test-timeout-[0-9]*:../../devel/py-test-timeout
TEST_DEPENDS+=	${PYPKGPREFIX}-dask-2022.9.1{,nb*}:../../pkgsrc_myownpkgs/py-dask
TEST_DEPENDS+=	${PYPKGPREFIX}-ipywidgets>=7.7.0:../../www/py-ipywidgets

USE_LANGUAGES=	# none
post-install:
	cd ${DESTDIR}${PREFIX} && \
	${MV} bin/dask-scheduler bin/dask-scheduler-${PYVERSSUFFIX} && \
	${MV} bin/dask-ssh bin/dask-ssh-${PYVERSSUFFIX} && \
	${MV} bin/dask-worker bin/dask-worker-${PYVERSSUFFIX} || ${TRUE}
	cd ${DESTDIR}${PREFIX}/lib/python${PYVERSSUFFIX}/site-packages && \
	${MV} -i distributed-*/* distributed
	cd ${DESTDIR}${PREFIX}/lib/python${PYVERSSUFFIX}/site-packages && \
	${RM} -rf distributed-*

do-test:
	cd ${WRKSRC} && ${SETENV} ${TEST_ENV} ${PYTHONBIN} -m pytest -s

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
