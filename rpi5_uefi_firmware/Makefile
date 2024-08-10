# $NetBSD$

GITHUB_PROJECT=	rpi5-uefi
DISTNAME=	RPi5_UEFI_Release_v0.3
PKGNAME=	${DISTNAME:S/Release_v/Firmware-/}
CATEGORIES=	devel
MASTER_SITES=	${MASTER_SITE_GITHUB:=worproject/}
GITHUB_RELEASE=	v0.3
EXTRACT_SUFX=	.zip
DIST_SUBDIR=	${GITHUB_PROJECT}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/worproject/rpi5-uefi/
COMMENT=	Raspberry Pi 5 UEFI Firmware Images
LICENSE=	2-clause-bsd

WRKSRC=		${WRKDIR}
USE_LANGUAGES=	# none

NO_BUILD=	yes

do-install:
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/rpi5_firmware
	${INSTALL_DATA} ${WRKSRC}/RPI_EFI.fd ${DESTDIR}${PREFIX}/share/rpi5_firmware
	${INSTALL_DATA} ${WRKSRC}/bcm2712-rpi-5-b.dtb ${DESTDIR}${PREFIX}/share/rpi5_firmware
	${INSTALL_DATA} ${WRKSRC}/config.txt ${DESTDIR}${PREFIX}/share/rpi5_firmware

.include "../../mk/bsd.pkg.mk"
