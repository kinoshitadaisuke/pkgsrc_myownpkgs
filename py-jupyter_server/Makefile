# $NetBSD$

DISTNAME=	jupyter_server-2.6.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=j/jupyter_server/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/jupyter_server/
COMMENT=	Backend for Jupyter web applications
LICENSE=	modified-bsd

DEPENDS+=	${PYPKGPREFIX}-hatchling>1.11:../../devel/py-hatchling
DEPENDS+=	${PYPKGPREFIX}-anyio>=3.1.0:../../devel/py-anyio
DEPENDS+=	${PYPKGPREFIX}-argon2-cffi>0:../../security/py-argon2-cffi
DEPENDS+=	${PYPKGPREFIX}-jinja2>0:../../textproc/py-jinja2
DEPENDS+=	${PYPKGPREFIX}-jupyter_client>=7.4.4:../../devel/py-jupyter_client
DEPENDS+=	${PYPKGPREFIX}-jupyter_core>=4.12:../../devel/py-jupyter_core
DEPENDS+=	${PYPKGPREFIX}-nbconvert>=6.4.4:../../www/py-nbconvert
DEPENDS+=	${PYPKGPREFIX}-nbformat>=5.3.0:../../www/py-nbformat
DEPENDS+=	${PYPKGPREFIX}-packaging>=21.3:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-prometheus_client>0:../../net/py-prometheus_client
DEPENDS+=	${PYPKGPREFIX}-zmq>=24.0.0:../../net/py-zmq
DEPENDS+=	${PYPKGPREFIX}-Send2Trash>0:../../sysutils/py-Send2Trash
DEPENDS+=	${PYPKGPREFIX}-terminado>=0.8.3:../../www/py-terminado
DEPENDS+=	${PYPKGPREFIX}-tornado>=6.2.0:../../www/py-tornado
DEPENDS+=	${PYPKGPREFIX}-traitlets>=5.6.0:../../devel/py-traitlets
DEPENDS+=	${PYPKGPREFIX}-websocket-client>0:../../www/py-websocket-client
DEPENDS+=	${PYPKGPREFIX}-jupyter_events>=0.6.0:../../pkgsrc_myownpkgs/py-jupyter_events
DEPENDS+=	${PYPKGPREFIX}-overrides>0:../../pkgsrc_myownpkgs/py-overrides
DEPENDS+=	${PYPKGPREFIX}-jupyter_packaging>0:../../pkgsrc_myownpkgs/py-jupyter_packaging
DEPENDS+=	${PYPKGPREFIX}-tomlkit>0:../../textproc/py-tomlkit
DEPENDS+=	${PYPKGPREFIX}-wheel>0:../../devel/py-wheel
DEPENDS+=	${PYPKGPREFIX}-hatch_jupyter_builder>0:../../pkgsrc_myownpkgs/py-hatch_jupyter_builder

PYTHON_VERSIONS_INCOMPATIBLE=	27

USE_PKGLOCALEDIR=	yes
USE_LANGUAGES=		# none

post-install:
.for name in server
	cd ${DESTDIR}${PREFIX}/bin && \
	${MV} jupyter-${name} jupyter-${name}-${PYVERSSUFFIX} || ${TRUE}
.endfor

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
