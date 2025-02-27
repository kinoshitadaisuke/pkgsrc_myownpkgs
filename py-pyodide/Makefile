# $NetBSD$

GITHUB_PROJECT=	pyodide
DISTNAME=	0.27.3
GITHUB_TAG=	refs/tags/${DISTNAME}
PKGNAME=	${PYPKGPREFIX}-${GITHUB_PROJECT}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_GITHUB:=pyodide/}
DIST_SUBDIR=	${GITHUB_PROJECT}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/pyodide/pyodide/
COMMENT=	Python distribution for browser and Node.js based on WebAssembly
LICENSE=	mpl-2.0

WRKSRC=		${WRKDIR}/${GITHUB_PROJECT}-${DISTNAME}
USE_LANGUAGES=	c c++

DEPENDS+=	cmake>=0:../../devel/cmake
DEPENDS+=	${PYPKGPREFIX}-ruamel-yaml>=0:../../devel/py-ruamel-yaml
DEPENDS+=	${PYPKGPREFIX}-pre-commit>=0:../../wip/py-pre-commit
DEPENDS+=	${PYPKGPREFIX}-build>=0.7.0:../../devel/py-build
DEPENDS+=	${PYPKGPREFIX}-sphinx-click>=0:../../pkgsrc_myownpkgs/py-sphinx-click
DEPENDS+=	${PYPKGPREFIX}-hypothesis>=0:../../devel/py-hypothesis
DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test
DEPENDS+=	${PYPKGPREFIX}-test-asyncio>=0:../../devel/py-test-asyncio
DEPENDS+=	${PYPKGPREFIX}-test-cov>=0:../../devel/py-test-cov
DEPENDS+=	${PYPKGPREFIX}-test-httpserver>=0:../../devel/py-test-httpserver
DEPENDS+=	${PYPKGPREFIX}-test-benchmark>=0:../../devel/py-test-benchmark

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
