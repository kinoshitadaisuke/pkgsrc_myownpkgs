# $NetBSD$

BOOK_B2E=	Biology2e-WEB.pdf
BOOK_BAP=	APBiology-OP_5meoFaG.pdf
BOOK_COB=	ConceptsofBiology-WEB.pdf
BOOK_IBN=	Introduction_to_Behavioral_Neuroscience-WEB.pdf
BOOK_MB=	Microbiology-WEB.pdf

DISTNAME=	# empty
PKGNAME=	openstax-science-biology-1.0
CATEGORIES=	math science
MASTER_SITES=	https://assets.openstax.org/oscms-prodcms/media/documents/
DISTFILES=	${BOOK_B2E} ${BOOK_BAP} ${BOOK_COB} ${BOOK_IBN} ${BOOK_MB}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://assets.openstax.org/oscms-prodcms/media/documents/
COMMENT=	OpenStax biology textbooks
LICENSE=	cc-by-v4.0

WRKSRC=		${WRKDIR}
USE_LANGUAGES=	# none

NO_BUILD=	yes

do-install:
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_B2E} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_BAP} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_COB} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_IBN} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_MB} ${DESTDIR}${PREFIX}/share/doc/openstax

.include "../../mk/bsd.pkg.mk"
