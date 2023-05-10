# $NetBSD$

DISTNAME=	async-lru-2.0.2
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	pkgsrc_myownpkgs python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/async-lru/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/async-lru/
COMMENT=	Simple lru cache for asyncio
LICENSE=	mit

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-flake8>=6.0.0:../../pkgsrc_myownpkgs/py-flake8
DEPENDS+=	${PYPKGPREFIX}-isort>=5.12.0:../../pkgsrc_myownpkgs/py-isort
DEPENDS+=	${PYPKGPREFIX}-black>=23.1.0:../../textproc/py-black
DEPENDS+=	${PYPKGPREFIX}-mypy>=1.0.1:../../pkgsrc_myownpkgs/py-mypy

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
