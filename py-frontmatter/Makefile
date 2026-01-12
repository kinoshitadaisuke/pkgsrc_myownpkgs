# $NetBSD$

DISTNAME=	frontmatter-3.0.8
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	textproc python
MASTER_SITES=	${MASTER_SITE_PYPI:=f/frontmatter/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/frontmatter/
COMMENT=	Package for parsing YAML Frontmatter from a text file or string
LICENSE=	isc

#DISTFILES=	${DEFAULT_DISTFILES}
#DISTFILES+=	LICENSE
#SITES.LICENSE=	https://raw.githubusercontent.com/jonbeebe/frontmatter/master/

#post-extract:
#	cd ${WRKSRC} && ${LN} -s ${WRKDIR}/LICENSE

DEPENDS+=	${PYPKGPREFIX}-yaml>=0:../../textproc/py-yaml

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
