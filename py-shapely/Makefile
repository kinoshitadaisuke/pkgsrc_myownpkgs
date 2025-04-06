# $NetBSD$

GITHUB_PROJECT=	shapely
DISTNAME=	2.1.0
GITHUB_TAG=	refs/tags/${DISTNAME}
PKGNAME=	${PYPKGPREFIX}-${GITHUB_PROJECT}-${DISTNAME}
CATEGORIES=	geography python
MASTER_SITES=	${MASTER_SITE_GITHUB:=shapely/}
DIST_SUBDIR=	${GITHUB_PROJECT}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/shapely/shapely/
COMMENT=	Manipulation and analysis of geometric objects
LICENSE=	modified-bsd

WRKSRC=	${WRKDIR}/${GITHUB_PROJECT}-${DISTNAME}

# url2pkg-marker (please do not remove this line.)
.include "../../geography/geos/buildlink3.mk"
.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
