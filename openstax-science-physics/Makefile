# $NetBSD$

BOOK_UP1=	University_Physics_Volume_1_-_WEB.pdf
BOOK_UP2=	University_Physics_Volume_2_-_WEB.pdf
BOOK_UP3=	UniversityPhysicsVolume3-WEB.pdf
BOOK_CP2E=	College_Physics_2e-WEB_7Zesafu.pdf
BOOK_CPAP2E=	College_Physics_for_AP_Courses_2e-WEB_DkhNbxV.pdf

DISTNAME=	# empty
PKGNAME=	openstax-science-physics-1.0
CATEGORIES=	math science
MASTER_SITES=	https://assets.openstax.org/oscms-prodcms/media/documents/
DISTFILES=	${BOOK_UP1} ${BOOK_UP2} ${BOOK_UP3} ${BOOK_CP2E} ${BOOK_CPAP2E}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://assets.openstax.org/oscms-prodcms/media/documents/
COMMENT=	OpenStax Physics textbooks
LICENSE=	cc-by-v4.0

WRKSRC=		${WRKDIR}
USE_LANGUAGES=	# none

NO_BUILD=	yes

do-install:
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_UP1} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_UP2} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_UP3} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_CP2E} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_CPAP2E} ${DESTDIR}${PREFIX}/share/doc/openstax

.include "../../mk/bsd.pkg.mk"
