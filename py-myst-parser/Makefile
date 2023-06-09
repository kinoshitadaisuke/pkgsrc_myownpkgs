# $NetBSD$

GITHUB_TAG=	refs/tags/v${PKGVERSION_NOREV}
DISTNAME=	MyST-Parser-1.0.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:tl}
CATEGORIES=	textproc python
MASTER_SITES=	${MASTER_SITE_GITHUB:=executablebooks/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/executablebooks/MyST-Parser/
COMMENT=	MyST is a rich and extensible flavor of Markdown
LICENSE=	mit

USE_PKGLOCALEDIR=	yes
USE_LANGUAGES=		# none

WRKSRC=	${WRKDIR}/${DISTNAME}

PYTHON_VERSIONS_INCOMPATIBLE=	27 37

DEPENDS+=	${PYPKGPREFIX}-flit_core>=3.4:../../devel/py-flit_core
DEPENDS+=	${PYPKGPREFIX}-docutils>=0.16:../../textproc/py-docutils
DEPENDS+=	${PYPKGPREFIX}-jinja2>=0:../../textproc/py-jinja2
DEPENDS+=	${PYPKGPREFIX}-markdown-it-py>=3.0:../../textproc/py-markdown-it-py
DEPENDS+=	${PYPKGPREFIX}-yaml>=0:../../textproc/py-yaml
DEPENDS+=       ${PYPKGPREFIX}-sphinx>=6:../../textproc/py-sphinx
DEPENDS+=	${PYPKGPREFIX}-pre-commit>=0:../../wip/py-pre-commit

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
