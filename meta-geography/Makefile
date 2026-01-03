# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-geography-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs geography
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for geography
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# geography
DEPENDS+=	garmin-utils>=0:../../geography/garmin-utils
DEPENDS+=	garmintools>=0:../../geography/garmintools
DEPENDS+=	gpsbabel>=0:../../geography/gpsbabel
DEPENDS+=	gpsutils>=0:../../geography/gpsutils
DEPENDS+=	viking>=0:../../geography/viking

# pkgsrc_myownpkgs
DEPENDS+=	${PYPKGPREFIX}-bmi-topography>=0:../../pkgsrc_myownpkgs/py-bmi-topography
DEPENDS+=	${PYPKGPREFIX}-contextily>=0:../../pkgsrc_myownpkgs/py-contextily
DEPENDS+=	${PYPKGPREFIX}-dtmdl>=0:../../pkgsrc_myownpkgs/py-dtmdl
DEPENDS+=	${PYPKGPREFIX}-elevation>=0:../../pkgsrc_myownpkgs/py-elevation
DEPENDS+=	${PYPKGPREFIX}-geographiclib>=0:../../pkgsrc_myownpkgs/py-geographiclib
DEPENDS+=	${PYPKGPREFIX}-geopy>=0:../../pkgsrc_myownpkgs/py-geopy
DEPENDS+=	${PYPKGPREFIX}-gmt>=0:../../pkgsrc_myownpkgs/py-gmt
DEPENDS+=	${PYPKGPREFIX}-gpxpy>=0:../../pkgsrc_myownpkgs/py-gpxpy
DEPENDS+=	${PYPKGPREFIX}-mercantile>=0:../../pkgsrc_myownpkgs/py-mercantile
DEPENDS+=	${PYPKGPREFIX}-osmnx>=0:../../pkgsrc_myownpkgs/py-osmnx
DEPENDS+=	${PYPKGPREFIX}-openeo-python-client>=0:../../pkgsrc_myownpkgs/py-openeo-python-client
DEPENDS+=	${PYPKGPREFIX}-rasterio>=0:../../pkgsrc_myownpkgs/py-rasterio
DEPENDS+=	${PYPKGPREFIX}-xyzservices>=0:../../pkgsrc_myownpkgs/py-xyzservices

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
