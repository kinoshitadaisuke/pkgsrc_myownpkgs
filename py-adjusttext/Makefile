# $NetBSD$

GITHUB_PROJECT=	adjustText
DISTNAME=	0.8.0
GITHUB_TAG=	refs/tags/${DISTNAME}
PKGNAME=	${PYPKGPREFIX}-${GITHUB_PROJECT:tl}-${DISTNAME}
CATEGORIES=	graphics python
MASTER_SITES=	${MASTER_SITE_GITHUB:=Phlya/}
DIST_SUBDIR=	${GITHUB_PROJECT}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/Phlya/adjustText
COMMENT=	Adjusting text position in matplotlib plots to minimize overlaps
LICENSE=	mit

DEPENDS+=	${PYPKGPREFIX}-matplotlib>=0:../../graphics/py-matplotlib
DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-bioframe>=0:../../pkgsrc_myownpkgs/py-bioframe
DEPENDS+=	${PYPKGPREFIX}-scipy>=0:../../math/py-scipy

WRKSRC=		${WRKDIR}/${GITHUB_PROJECT}-${DISTNAME}
USE_LANGUAGES=	# none

BUILDLINK_API_DEPENDS.py-numpy+=	${PYPKGPREFIX}-numpy>=0

.include "../../math/py-numpy/buildlink3.mk"
# TODO: Migrate MASTER_SITES to MASTER_SITE_PYPI
.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
