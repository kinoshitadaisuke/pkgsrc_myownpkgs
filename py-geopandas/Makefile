# $NetBSD$

GITHUB_PROJECT=	geopandas
DISTNAME=	1.1.1
GITHUB_TAG=	refs/tags/v${PKGVERSION_NOREV}
PKGNAME=	${PYPKGPREFIX}-${GITHUB_PROJECT}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_GITHUB:=geopandas/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/geopandas/geopandas/
COMMENT=	adding support for geographic data to pandas objects
LICENSE=	modified-bsd

WRKSRC=	${WRKDIR}/${GITHUB_PROJECT}-${DISTNAME}

DEPENDS+=	${PYPKGPREFIX}-packaging>=0:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-pandas>=1.4.0:../../math/py-pandas
DEPENDS+=	${PYPKGPREFIX}-proj>=3.2.0:../../geography/py-proj
DEPENDS+=	${PYPKGPREFIX}-geodatasets>=0:../../pkgsrc_myownpkgs/py-geodatasets
DEPENDS+=	${PYPKGPREFIX}-pyogrio>=0:../../pkgsrc_myownpkgs/py-pyogrio
DEPENDS+=	${PYPKGPREFIX}-shapely>=1.7.0:../../pkgsrc_myownpkgs/py-shapely
DEPENDS+=	naturalearth-10m>=5.1.1:../../pkgsrc_myownpkgs/naturalearth-10m

# url2pkg-marker (please do not remove this line.)
.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
