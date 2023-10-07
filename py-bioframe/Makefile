# $NetBSD$

GITHUB_PROJECT=	bioframe
DISTNAME=	0.5.0
GITHUB_TAG=	refs/tags/v${DISTNAME}
PKGNAME=	${PYPKGPREFIX}-${GITHUB_PROJECT}-${DISTNAME}
CATEGORIES=	graphics python
MASTER_SITES=	${MASTER_SITE_GITHUB:=open2c/}
DIST_SUBDIR=	${GITHUB_PROJECT}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/open2c/bioframe
COMMENT=	Pandas utilities for tab-delimited and other genomic files
LICENSE=	mit

WRKSRC=	${WRKDIR}/${GITHUB_PROJECT}-${DISTNAME}

PYTHON_VERSIONS_INCOMPATIBLE=	27

BUILD_DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel
BUILD_DEPENDS+=	${PYPKGPREFIX}-hatchling>=0:../../devel/py-hatchling
BUILD_DEPENDS+=	${PYPKGPREFIX}-hatch-vcs>=0:../../devel/py-hatch-vcs
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=0:../../graphics/py-matplotlib
DEPENDS+=	${PYPKGPREFIX}-pandas>=1.3:../../math/py-pandas
DEPENDS+=	${PYPKGPREFIX}-yaml>=0:../../textproc/py-yaml
DEPENDS+=	${PYPKGPREFIX}-requests>=0:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=0:../../devel/py-typing-extensions
TEST_DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test

USE_LANGUAGES=	# none

BUILDLINK_API_DEPENDS.py-numpy+=	${PYPKGPREFIX}-numpy>=1.10

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
