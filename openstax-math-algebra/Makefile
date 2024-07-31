# $NetBSD$

BOOK_ONE=	Algebra-and-Trigonometry-2e-WEB.pdf
BOOK_TWO=	College-Algebra-2e-WEB.pdf
BOOK_THREE=	College-Algebra-Corequisite-Support-2e-WEB.pdf
BOOK_FOUR=	ElementaryAlgebra2e-WEB_3zxfu3Z.pdf
BOOK_FIVE=	IntermediateAlgebra2e-WEB_RlpFLLx.pdf
BOOK_SIX=	Prealgebra2e-WEB_0qbw93r.pdf

DISTNAME=	# empty
PKGNAME=	openstax-math-algebra-1.0
CATEGORIES=	math science
MASTER_SITES=	https://assets.openstax.org/oscms-prodcms/media/documents/
DISTFILES=	${BOOK_ONE} ${BOOK_TWO} ${BOOK_THREE} ${BOOK_FOUR} ${BOOK_FIVE} ${BOOK_SIX}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://assets.openstax.org/oscms-prodcms/media/documents/
COMMENT=	OpenStax Algebra textbooks
LICENSE=	cc-by-v4.0

WRKSRC=		${WRKDIR}
USE_LANGUAGES=	# none

NO_BUILD=	yes

do-install:
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_ONE} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_TWO} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_THREE} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_FOUR} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_FIVE} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_SIX} ${DESTDIR}${PREFIX}/share/doc/openstax

.include "../../mk/bsd.pkg.mk"
