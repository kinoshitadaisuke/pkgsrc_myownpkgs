# $NetBSD$

DISTNAME=	master
PKGNAME=	tex-kmbeamer-0.0
CATEGORIES=	print
MASTER_SITES=	https://github.com/kmaed/kmbeamer/archive/
EXTRACT_SUFX=	.zip

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kmaed/kmbeamer/
COMMENT=	Mr. Kazuki Maeda's Beamer themes
LICENSE=	mit

WRKSRC=		${WRKDIR}/kmbeamer-master

TEXLIVE_UNVERSIONED=	YES

DEPENDS+=	tex-beamer>=0:../../print/tex-beamer
DEPENDS+=	tex-svgcolor>=0:../../pkgsrc_myownpkgs/tex-svgcolor

post-extract:
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/texmf-dist/tex/latex/kmbeamer
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/texmf-dist/tex/latex/kmbeamer/kmbeamer_bg
	${INSTALL_DATA} ${WRKSRC}/*.sty ${DESTDIR}${PREFIX}/share/texmf-dist/tex/latex/kmbeamer
	${INSTALL_DATA} ${WRKSRC}/kmbeamer_bg/* ${DESTDIR}${PREFIX}/share/texmf-dist/tex/latex/kmbeamer/kmbeamer_bg

# url2pkg-marker (please do not remove this line.)
.include "../../print/texlive/package.mk"
.include "../../mk/bsd.pkg.mk"
