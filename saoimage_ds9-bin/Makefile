# $NetBSD$

DISTNAME=	ds9.opensuse15x86.8.6
PKGNAME=	${DISTNAME:S/ds9.opensuse15x86./saoimage_ds9-bin-/}
CATEGORIES=	math
MASTER_SITES=	https://ds9.si.edu/download/opensuse15x86/

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://ds9.si.edu/download/opensuse15/
COMMENT=	Image display and visualization tool for astronomical data
LICENSE=	gnu-gpl-v3

WRKSRC=		${WRKDIR}
USE_LANGUAGES=	# none

#EMUL_MODULES.linux=	base
EMUL_PLATFORMS=	linux-x86_64
NO_CONFIGURE=	yes
NO_BUILD=	yes

DEPENDS+=	suse_base>=15:../../emulators/suse15_base
DEPENDS+=	suse_fontconfig>=15:../../emulators/suse15_fontconfig
DEPENDS+=	suse_libxml2>=15:../../emulators/suse15_libxml2
DEPENDS+=	suse_x11>=15:../../emulators/suse15_x11

do-install:
	${MKDIR} ${DESTDIR}${PREFIX}/bin
	${CP} ${WRKSRC}/ds9 ${DESTDIR}${PREFIX}/bin/ds9-bin
	#${INSTALL_PROGRAM} ${WRKSRC}/ds9 ${DESTDIR}${PREFIX}/bin/ds9-bin

.include "../../x11/tk/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
