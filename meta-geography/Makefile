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

.include "../../mk/bsd.pkg.mk"
