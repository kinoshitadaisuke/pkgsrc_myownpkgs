# $NetBSD$

VOL_ONE=	UniversityPhysicsVol1-WEB.pdf
VOL_TWO=	UniversityPhysicsVolume2-WEB_5eNhMSa.pdf
VOL_THREE=	UniversityPhysicsVolume3-WEB.pdf

DISTNAME=	# empty
PKGNAME=	openstax-science-university-physics-1.0
CATEGORIES=	math science
MASTER_SITES=	https://assets.openstax.org/oscms-prodcms/media/documents/
DISTFILES=	${VOL_ONE} ${VOL_TWO} ${VOL_THREE}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://assets.openstax.org/oscms-prodcms/media/documents/
COMMENT=	OpenStax University Physics textbooks
LICENSE=	cc-by-v4.0

WRKSRC=		${WRKDIR}
USE_LANGUAGES=	# none

NO_BUILD=	yes

do-install:
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${VOL_ONE} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${VOL_TWO} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${VOL_THREE} ${DESTDIR}${PREFIX}/share/doc/openstax

.include "../../mk/bsd.pkg.mk"
