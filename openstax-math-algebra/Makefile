# $NetBSD$

BOOK_AT2E=	algebra-and-trigonometry-2e_-_WEB.pdf
BOOK_CA2E=	college-algebra-2e_-_WEB.pdf
BOOK_CACS2E=	college-algebra-corequisite-support-2e_-_WEB.pdf
BOOK_EA2E=	elementary-algebra-2e_-_WEB.pdf
BOOK_IA2E=	intermediate-algebra-2e_-_WEB.pdf
BOOK_PA2E=	prealgebra-2e_-_WEB.pdf
BOOK_HSA1=	algebra-1_-_WEB.pdf

DISTNAME=	# empty
PKGNAME=	openstax-math-algebra-1.0
CATEGORIES=	math science
MASTER_SITES=	https://assets.openstax.org/oscms-prodcms/media/documents/
DISTFILES=	${BOOK_AT2E} ${BOOK_CA2E} ${BOOK_CACS2E} ${BOOK_EA2E} ${BOOK_IA2E} ${BOOK_PA2E} ${BOOK_HSA1}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://assets.openstax.org/oscms-prodcms/media/documents/
COMMENT=	OpenStax Algebra textbooks
LICENSE=	cc-by-v4.0

WRKSRC=		${WRKDIR}
USE_LANGUAGES=	# none

NO_BUILD=	yes

do-install:
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_AT2E} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_CA2E} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_CACS2E} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_EA2E} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_IA2E} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_PA2E} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_HSA1} ${DESTDIR}${PREFIX}/share/doc/openstax

.include "../../mk/bsd.pkg.mk"
