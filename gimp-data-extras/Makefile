# $NetBSD$

DISTNAME=	gimp-data-extras-2.0.4
CATEGORIES=	graphics
MASTER_SITES=	https://download.gimp.org/gimp/extras/
EXTRACT_SUFX=	.tar.bz2

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://download.gimp.org/gimp/extras/
COMMENT=	Extra data for Gimp
LICENSE=	gpl-3.0

NO_BUILD=	yes

do-install:
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/gimp/2.0/scripts
	${INSTALL_DATA} ${WRKSRC}/scripts/*.scm ${DESTDIR}${PREFIX}/share/gimp/2.0/scripts

.include "../../mk/bsd.pkg.mk"
