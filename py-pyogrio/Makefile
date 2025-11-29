# $NetBSD$

DISTNAME=	pyogrio-0.12.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	geography
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pyogrio/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/pyogrio/
COMMENT=	Vectorized spatial vector file format I/O using GDAL/OGR
LICENSE=	mit

DEPENDS+=	${PYPKGPREFIX}-gdal>=3.4.0:../../geography/py-gdal

# url2pkg-marker (please do not remove this line.)
.include "../../geography/gdal-lib/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
