# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-raspberrypi-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs sysutils
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for  Raspberry Pi
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# pkgsrc_myownpkgs
DEPENDS+=	rpi3_uefi_firmware>=0:../../pkgsrc_myownpkgs/rpi3_uefi_firmware
DEPENDS+=	rpi4_uefi_firmware>=0:../../pkgsrc_myownpkgs/rpi4_uefi_firmware
DEPENDS+=	rpi5_uefi_firmware>=0:../../pkgsrc_myownpkgs/rpi5_uefi_firmware

.include "../../mk/bsd.pkg.mk"
