# $NetBSD$

GITHUB_PROJECT=	RPi4
GITHUB_RELEASE=	v1.39
DISTNAME=	${GITHUB_PROJECT}_UEFI_Firmware_${GITHUB_RELEASE}
PKGNAME=	${DISTNAME:S/_v/-/}
CATEGORIES=	devel
MASTER_SITES=	${MASTER_SITE_GITHUB:=pftf/}
EXTRACT_SUFX=	.zip

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/pftf/RPi4/
COMMENT=	Raspberry Pi 4 UEFI Firmware Images
LICENSE=	2-clause-bsd

WRKSRC=		${WRKDIR}
USE_LANGUAGES=	# none

NO_BUILD=	yes
INSTALLATION_DIRS=	firmware firmware/brcm overlays

do-install:
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/rpi4_firmware/firmware/brcm
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/rpi4_firmware/overlays
	${INSTALL_DATA} ${WRKSRC}/RPI_EFI.fd ${DESTDIR}${PREFIX}/share/rpi4_firmware
	${INSTALL_DATA} ${WRKSRC}/Readme.md ${DESTDIR}${PREFIX}/share/rpi4_firmware
	${INSTALL_DATA} ${WRKSRC}/bcm2711-rpi-4-b.dtb ${DESTDIR}${PREFIX}/share/rpi4_firmware
	${INSTALL_DATA} ${WRKSRC}/bcm2711-rpi-400.dtb ${DESTDIR}${PREFIX}/share/rpi4_firmware
	${INSTALL_DATA} ${WRKSRC}/bcm2711-rpi-cm4.dtb ${DESTDIR}${PREFIX}/share/rpi4_firmware
	${INSTALL_DATA} ${WRKSRC}/config.txt ${DESTDIR}${PREFIX}/share/rpi4_firmware
	${INSTALL_DATA} ${WRKSRC}/fixup4.dat ${DESTDIR}${PREFIX}/share/rpi4_firmware
	${INSTALL_DATA} ${WRKSRC}/start4.elf ${DESTDIR}${PREFIX}/share/rpi4_firmware
	${INSTALL_DATA} ${WRKSRC}/firmware/LICENCE.txt ${DESTDIR}${PREFIX}/share/rpi4_firmware/firmware
	${INSTALL_DATA} ${WRKSRC}/firmware/Readme.txt ${DESTDIR}${PREFIX}/share/rpi4_firmware/firmware
	${INSTALL_DATA} ${WRKSRC}/firmware/brcm/brcmfmac43455-sdio.Raspberry ${DESTDIR}${PREFIX}/share/rpi4_firmware/firmware/brcm
	${INSTALL_DATA} ${WRKSRC}/firmware/brcm/brcmfmac43455-sdio.bin ${DESTDIR}${PREFIX}/share/rpi4_firmware/firmware/brcm
	${INSTALL_DATA} ${WRKSRC}/firmware/brcm/brcmfmac43455-sdio.clm_blob ${DESTDIR}${PREFIX}/share/rpi4_firmware/firmware/brcm
	${INSTALL_DATA} ${WRKSRC}/firmware/brcm/brcmfmac43455-sdio.txt ${DESTDIR}${PREFIX}/share/rpi4_firmware/firmware/brcm
	${INSTALL_DATA} ${WRKSRC}/overlays/miniuart-bt.dtbo ${DESTDIR}${PREFIX}/share/rpi4_firmware/firmware/brcm
	${INSTALL_DATA} ${WRKSRC}/overlays/upstream-pi4.dtbo ${DESTDIR}${PREFIX}/share/rpi4_firmware/firmware/brcm

.include "../../mk/bsd.pkg.mk"
