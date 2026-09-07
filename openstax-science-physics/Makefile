# $NetBSD$

BOOK_UP1=	university-physics-volume-1_-_WEB.pdf
BOOK_UP2=	university-physics-volume-2_-_WEB.pdf
BOOK_UP3=	university-physics-volume-3_-_WEB.pdf
BOOK_CP2E=	college-physics-2e_-_WEB.pdf
BOOK_CPAP2E=	college-physics-ap-courses-2e_-_WEB.pdf

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
