# $NetBSD$

GITHUB_TAG=	refs/tags/v${PKGVERSION_NOREV}
DISTNAME=	jupyter-cache-0.6.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_GITHUB:=executablebooks/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/executablebooks/jupyter-cache/
COMMENT=	Defined interface for working with a cache of jupyter notebooks
LICENSE=	mit

WRKSRC=	${WRKDIR}/${DISTNAME}

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27 37

DEPENDS+=	${PYPKGPREFIX}-flit_core>=3.4:../../devel/py-flit_core
DEPENDS+=	${PYPKGPREFIX}-attrs>=0:../../devel/py-attrs
DEPENDS+=	${PYPKGPREFIX}-click>=0:../../devel/py-click
DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>=0:../../devel/py-importlib-metadata
DEPENDS+=	${PYPKGPREFIX}-nbclient>=0.2:../../www/py-nbclient
DEPENDS+=	${PYPKGPREFIX}-nbformat>=0:../../www/py-nbformat
DEPENDS+=	${PYPKGPREFIX}-yaml>=0:../../textproc/py-yaml
DEPENDS+=	${PYPKGPREFIX}-sqlalchemy>=1.3.12:../../databases/py-sqlalchemy
DEPENDS+=	${PYPKGPREFIX}-tabulate>=0:../../textproc/py-tabulate
DEPENDS+=	${PYPKGPREFIX}-click-log>=0:../../devel/py-click-log
DEPENDS+=	${PYPKGPREFIX}-pre-commit>=0:../../wip/py-pre-commit

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
