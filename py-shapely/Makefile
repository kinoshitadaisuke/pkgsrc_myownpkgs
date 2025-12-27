# $NetBSD$

DISTNAME=	shapely-2.1.2
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	geography math python
MASTER_SITES=	${MASTER_SITE_PYPI:=s/shapely/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/shapely/
COMMENT=	Manipulation and analysis of geometric objects
LICENSE=	modified-bsd

#WRKSRC=	${WRKDIR}/${GITHUB_PROJECT}-${DISTNAME}

# url2pkg-marker (please do not remove this line.)
.include "../../geography/geos/buildlink3.mk"
.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
