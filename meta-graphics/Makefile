# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-graphics-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs graphics
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for graphics applications
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# graphics
DEPENDS+=	ImageMagick>=0:../../graphics/ImageMagick
DEPENDS+=	dcraw>=0:../../graphics/dcraw
DEPENDS+=	exif>=0:../../graphics/exif
DEPENDS+=	feh>=0:../../graphics/feh
DEPENDS+=	gimp>=0:../../graphics/gimp
DEPENDS+=	inkscape>=0:../../graphics/inkscape
DEPENDS+=	jhead>=0:../../graphics/jhead
DEPENDS+=	netpbm>=0:../../graphics/netpbm
DEPENDS+=	ps2eps>=0:../../graphics/ps2eps
#DEPENDS+=	skencil>=0:../../graphics/skencil
DEPENDS+=	tesseract>=0:../../graphics/tesseract
DEPENDS+=	tgif>=0:../../graphics/tgif
DEPENDS+=	xfig>=0:../../graphics/xfig
#DEPENDS+=	xpaint>=0:../../graphics/xpaint
DEPENDS+=	xv>=0:../../graphics/xv

# pkgsrc_myownpkgs
DEPENDS+=	gimp-data-extras>=0:../../pkgsrc_myownpkgs/gimp-data-extras

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
