# $NetBSD$

GITHUB_PROJECT=	RPi3
GITHUB_RELEASE=	v1.50
DISTNAME=	${GITHUB_PROJECT}_UEFI_Firmware_${GITHUB_RELEASE}
PKGNAME=	${DISTNAME:S/_v/-/tl}
CATEGORIES=	devel
MASTER_SITES=	${MASTER_SITE_GITHUB:=pftf/}
EXTRACT_SUFX=	.zip

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/pftf/RPi3/
COMMENT=	Raspberry Pi 3 UEFI Firmware Images
LICENSE=	2-clause-bsd

WRKSRC=		${WRKDIR}
USE_LANGUAGES=	# none

NO_BUILD=	yes
INSTALLATION_DIRS=	firmware

do-install:
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/rpi3_firmware/firmware
	${INSTALL_DATA} ${WRKSRC}/RPI_EFI.fd ${DESTDIR}${PREFIX}/share/rpi3_firmware
	${INSTALL_DATA} ${WRKSRC}/Readme.md ${DESTDIR}${PREFIX}/share/rpi3_firmware
	${INSTALL_DATA} ${WRKSRC}/bcm2710-rpi-3-b-plus.dtb ${DESTDIR}${PREFIX}/share/rpi3_firmware
	${INSTALL_DATA} ${WRKSRC}/bcm2710-rpi-3-b.dtb ${DESTDIR}${PREFIX}/share/rpi3_firmware
	${INSTALL_DATA} ${WRKSRC}/bcm2710-rpi-cm3.dtb ${DESTDIR}${PREFIX}/share/rpi3_firmware
	${INSTALL_DATA} ${WRKSRC}/bootcode.bin ${DESTDIR}${PREFIX}/share/rpi3_firmware
	${INSTALL_DATA} ${WRKSRC}/config.txt ${DESTDIR}${PREFIX}/share/rpi3_firmware
	${INSTALL_DATA} ${WRKSRC}/fixup.dat ${DESTDIR}${PREFIX}/share/rpi3_firmware
	${INSTALL_DATA} ${WRKSRC}/start.elf ${DESTDIR}${PREFIX}/share/rpi3_firmware
	${INSTALL_DATA} ${WRKSRC}/firmware/LICENCE_bin+clm_blob.txt ${DESTDIR}${PREFIX}/share/rpi3_firmware/firmware
	${INSTALL_DATA} ${WRKSRC}/firmware/LICENSE_txt.txt ${DESTDIR}${PREFIX}/share/rpi3_firmware/firmware
	${INSTALL_DATA} ${WRKSRC}/firmware/Readme.txt ${DESTDIR}${PREFIX}/share/rpi3_firmware/firmware
	${INSTALL_DATA} ${WRKSRC}/firmware/brcmfmac43430-sdio.bin ${DESTDIR}${PREFIX}/share/rpi3_firmware/firmware
	${INSTALL_DATA} ${WRKSRC}/firmware/brcmfmac43430-sdio.clm_blob ${DESTDIR}${PREFIX}/share/rpi3_firmware/firmware
	${INSTALL_DATA} ${WRKSRC}/firmware/brcmfmac43430-sdio.txt ${DESTDIR}${PREFIX}/share/rpi3_firmware/firmware
	${INSTALL_DATA} ${WRKSRC}/firmware/brcmfmac43455-sdio.bin ${DESTDIR}${PREFIX}/share/rpi3_firmware/firmware
	${INSTALL_DATA} ${WRKSRC}/firmware/brcmfmac43455-sdio.clm_blob ${DESTDIR}${PREFIX}/share/rpi3_firmware/firmware
	${INSTALL_DATA} ${WRKSRC}/firmware/brcmfmac43455-sdio.txt ${DESTDIR}${PREFIX}/share/rpi3_firmware/firmware

.include "../../mk/bsd.pkg.mk"
