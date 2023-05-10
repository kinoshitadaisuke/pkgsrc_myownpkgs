# $NetBSD$

GITHUB_PROJECT=	XEphem
GITHUB_TAG=	refs/tags/4.1.0
DISTNAME=	4.1.0
PKGNAME=	${GITHUB_PROJECT:tl}-${DISTNAME}
CATEGORIES=	pkgsrc_myownpkgs
MASTER_SITES=	${MASTER_SITE_GITHUB:=XEphem/}
DIST_SUBDIR=	${GITHUB_PROJECT}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/XEphem/XEphem/
COMMENT=	Interactive astronomy program for all UNIX platforms
LICENSE=	mit

WRKSRC=			${WRKDIR}/${GITHUB_PROJECT}-${DISTNAME}
BUILD_DIRS+=		GUI/xephem
X11_LDFLAGS+=		${LIBS}
MAKE_ENV+=		X11_LDFLAGS=${X11_LDFLAGS:Q}
USE_TOOLS+=		gmake
USE_TOOLS+=		perl:run
USE_TOOLS+=		pax
REPLACE_INTERPRETER+=	perl
REPLACE_PERL+=		auxil/*.pl
REPLACE.perl.old=	.*/bin/perl
REPLACE.perl.new=	${PREFIX}/bin/perl
REPLACE_FILES.perl=	GUI/xephem/auxil/astorb2edb.pl \
			GUI/xephem/auxil/mpcorb2edb.pl


INSTALLATION_DIRS=	bin \
			lib/X11/app-defaults \
			share/xephem \
			${PKGMANDIR}/man1

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/GUI/xephem/xephem ${DESTDIR}${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/GUI/xephem/xephem.man ${DESTDIR}${PREFIX}/${PKGMANDIR}/man1/xephem.1
	${SED} s,@PREFIX@,${PREFIX}, ${FILESDIR}/XEphem.ad > ${WRKDIR}/XEphem
	${INSTALL_DATA} ${WRKDIR}/XEphem ${DESTDIR}${PREFIX}/lib/X11/app-defaults
	cd ${WRKSRC}/GUI/xephem; \
	pax -rw auxil catalogs fifos fits gallery help lo \
	${DESTDIR}${PREFIX}/share/xephem

.include "../../x11/libX11/buildlink3.mk"
.include "../../x11/libXext/buildlink3.mk"
.include "../../x11/libXmu/buildlink3.mk"
.include "../../x11/libXt/buildlink3.mk"
.include "../../mk/motif.buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
